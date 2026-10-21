
import argparse
import os

from call_function import available_functions, call_function
from dotenv import load_dotenv
from openai import OpenAI

from prompts import system_prompt


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to the LLM")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_content(client, messages, args.verbose)


def generate_content(client: OpenAI, messages: list, verbose: bool) -> None:
    for _ in range(20):
        response = client.chat.completions.create(
            model="minimax/minimax-m3.1-flash:free",
            messages=messages,
            tools=available_functions,
        )

        if not response.choices:
            raise RuntimeError("API response has no choices")

        if verbose and response.usage:
            print("Prompt tokens:", response.usage.prompt_tokens)
            print("Response tokens:", response.usage.completion_tokens)

        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            print("Final response:")
            print(message.content)
            return

        for tool_call in message.tool_calls:
            if tool_call.type != "function":
                raise RuntimeError("Unsupported tool call type")

            result_message = call_function(tool_call, verbose)

            if not result_message.get("content"):
                raise RuntimeError(
                    f"Empty function response for {tool_call.function.name}"
                )

            messages.append(result_message)

            if verbose:
                print(f"-> {result_message['content']}")

    raise RuntimeError("Agent exceeded 20 iterations")


if __name__ == "__main__":
    main()

