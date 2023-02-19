import sys, yaml

def block(yaml_document):
  def details(summary):
    details = yaml_document.get(summary)
    if details == None:
      return ''
    return (
      f'<details><summary>{summary}:</summary>\n\n'
      f'```bash\n'
      f'{details}\n'
      f'```\n'
      f'</details>\n\n'
    )
  title = f'\n---\n### {yaml_document.get("title", "")}\n'
  solutions = map(details, ('perl', 'python', 'canonical'))
  return title + ''.join(solutions)

def main():
  prologue, *blocks, epilogue = yaml.load_all(sys.stdin.read(), yaml.Loader)
  print(prologue, *map(block, blocks), epilogue, sep='\n\n')

main()
