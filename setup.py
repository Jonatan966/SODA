from cx_Freeze import setup, Executable
#Aqui onde contém o compilador do sistema

setup(
    name = "SODA",
    version = "1.6",
    description = "Um sistema para facilitar sua vida, futuramente sera uma linguagem de programacao",
    options = {"build_exe": {
        'packages': ["os","sys","math"],
        'include_files': ['documentacao.txt'],
        'include_msvcr': True,
    }},
    executables = [Executable("Smain.py",base="Console", icon='SODA.ico')]
    )