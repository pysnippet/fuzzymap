import re

if __name__ == "__main__":
    mermaid_snippet_pattern = r"^```mermaid[\s\S]+?```"
    mermaid_snippet_svg_url = (
        # Initially was uploaded to GitHub
        "https://user-images.githubusercontent.com/44609997/"
        "205437148-4fb3d7bd-1fe9-4ce8-8321-d7aef9488e37.svg"
    )
    html_replacement = "<p align=\"center\"><img src=\"%s\" height=\"400\" /></p>" % mermaid_snippet_svg_url
    with open("README.md", "r") as fp:
        readme = fp.read()
        readme = re.sub(mermaid_snippet_pattern, html_replacement, readme, flags=re.M)

    with open("README.md", "w") as fp:
        fp.write(readme)
