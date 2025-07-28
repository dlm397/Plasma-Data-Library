from config_loader import load_config, get_path, get_setting, get_home_path
import numpy as np # type: ignore

def save_data(data, file_name, path_key="data_dir"):
    save_location = get_path(path_key)
    save_type = get_setting("default_format")
    data_type = str(type(data))
    if data_type == "<class 'numpy.ndarray'>":
        np.savetxt(f"{save_location}\\{file_name}.{save_type}", data, delimiter=',')
        return (f"{save_location}\\{file_name}.{save_type}")
    elif data_type == "<class 'list'>":
        np.savetxt(f"{save_location}\\{file_name}.{save_type}", data, delimiter=',')
        return (f"{save_location}\\{file_name}.{save_type}")
    else:
        print(f"failed, file type {data_type},not acceptable file type indentified.")
        return 
    
    