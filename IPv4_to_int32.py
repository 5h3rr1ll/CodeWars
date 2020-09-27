def ip_to_int32(ip):
    ip_splitted = ip.split(".")
    lst_binaries = [f"{int(n):08b}" for n in ip_splitted]
    binary_str = "".join(lst_binaries)
    return int(binary_str, 2)
