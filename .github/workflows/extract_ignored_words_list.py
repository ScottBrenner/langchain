import toml

pyproject_toml = toml.load("pyproject.toml")

# Extract the ignore words list (adjust the key as per your TOML structure)
ignore_words_list = (
    pyproject_toml.get("tool", {}).get("codespell", {}).get("ignore-words-list")
)

with open(os.environ["GITHUB_OUTPUT"], "a") as file:
    print(f"ignore_words_list={ignore_words_list}", file=file)
