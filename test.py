

HYPEN_E_DOT = "-e ."

file_path = 'requirements.txt'
requirements = []
with open(file_path) as file:
    requirements = file.readlines()
    print("Requirements 1 :", requirements)
    requirements = [req.replace("\n", "") for req in requirements]
    print("Requirements 2 :", requirements)
    requirements = [req.strip() for req in requirements]
    print("Requirements stripped :", requirements)

    if(HYPEN_E_DOT in requirements):
        requirements.remove(HYPEN_E_DOT)
        print("Requirements 3 :", requirements)
