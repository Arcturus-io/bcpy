import subprocess
import os


def sqlcmd_caller(command_file_path):
    result = subprocess.run(['sqlcmd',
                    '-S', f'mssql-server,{os.environ["TEST_MSSQL_PORT"]}',
                    '-U', 'SA',
                    '-P', os.environ['TEST_MSSQL_SA_PASSWORD'],
                    '-i', command_file_path])
    if result.returncode != 0:
        raise Exception(result.stderr) # TODO find out why stderr is empty
