import glob
import os

def read_input_dir(path: str):
    """
    Accepts 'path' as argument and if the supplied path is a directory, loops over directories and returns all '.txt' files.
    
    Parameters:
        path (str): The directory path to search for '.txt' files.
    Returns:
        list: A list of file paths for all '.txt' files found in the directory.
    """
    files = [f for f in glob.glob(f"{path}/*.txt")]
    return files

def read_files(files):
    """
    Reads the content of each file in the list of file paths and returns a list of tuples
    containing the file names and their respective contents.

    Parameters:
        files (list): A list of file paths.
    Returns:
        list: A list of tuples containing the file names and their respective contents.
    """
    data = []
    for file in files:
        with open(file, 'r') as f:
            file_content = f.read()
            data.append((file, file_content))
    return data

def write_to_file(directory, file_name, content):
    """
    Write content to a text file within a specified directory.

    Parameters:
        directory (str): The path to the directory where the file will be created.
        file_name (str): The name of the file to be created.
        content (str): The content to be written to the file.
    
    Returns:
        None
    """
    file_name = os.path.basename(file_name)
    
    # Create the directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Construct the full file path
    file_path = os.path.join(directory, file_name)
    
    # Write content to the file
    with open(file_path, 'w') as file:
        file.write(content)
    
    file.close()
