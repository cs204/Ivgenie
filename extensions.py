def main():
    a = input("File name: ")
    a = a.split(".")
    b = len(a)
    match a[b - 1]:
        case "gif":
            print ("image/gif")
        case "jpg":
            print ("image/jpg")
        case "gpeg":
            print ("image/jpeg")
        case "png":
            print ("image/png")
        case "pdf":
            print ("application/pdf")
        case "txt":
            print ("application/txt")
        case "zip":
            print ("application/zip")
        case _:
            print("application/octet-stream")

main()