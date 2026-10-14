
import Pyro5.api


def main():
    try:
        # Connect to the Pyro5 Name Server
        ns = Pyro5.api.locate_ns(
            host="127.0.0.1",
            port=9000
        )

        # Look up the laptop remote object
        uri = ns.lookup("laptop")

        # Access product information remotely
        with Pyro5.api.Proxy(uri) as laptop:
            laptop_name = laptop.getName()
            laptop_description = laptop.getDescription()
            price = laptop.getPrice()

            print("Name: " + laptop_name)
            print("Description: " + laptop_description)
            print("Price: " + str(price))

    except Exception as e:
        print("Exception in client side:", e)


if __name__ == "__main__":
    main()
