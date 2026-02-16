def main():
    with open("video-314/numeros.bin", "wb") as f:
        numeros = [2, 3, 5, 7, 11]
        f.write(bytearray(numeros))  #   Escribe la lista al archivo

    with open("video-314/numeros.bin", "rb") as f:
        numeros = list(f.read())
        print(numeros)


if __name__ == "__main__":
    main()
