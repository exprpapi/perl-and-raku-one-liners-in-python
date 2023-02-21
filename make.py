import sys, yaml

def block(yaml_document):
  def details(solution):
    details = yaml_document.get(solution)
    return (
      f'<details><summary>{solution}:</summary>\n\n'
      f'```bash\n{details}\n```\n</details>\n\n'
    )

  title, *solutions = yaml_document.keys()
  title = f'\n---\n### {yaml_document.get(title)}\n'
  solutions = map(details, solutions)
  return title + ''.join(solutions)

def main():
  prologue, *blocks, epilogue = yaml.load_all(sys.stdin.read(), yaml.Loader)
  print(prologue, *map(block, blocks), epilogue, sep='\n\n')

main()
