
import Pyro5.api
from product import Product


def main():
    try:
        print("Server is booting....")

        # Create the product objects
        p1 = Product("Laptop", "Lenovo laptop", 800000.0)
        p2 = Product("Mobile", "MI 9 mobile", 24000.0)
        p3 = Product("Bag", "Branded bag", 800.0)
        p4 = Product("Charger", "MI Charger", 230.0)

        # Create the Pyro5 daemon
        daemon = Pyro5.api.Daemon(host="127.0.0.1")

        # Connect to the Pyro5 Name Server
        ns = Pyro5.api.locate_ns(
            host="127.0.0.1",
            port=9000
        )

        # Register product objects with the daemon
        uri1 = daemon.register(p1)
        uri2 = daemon.register(p2)
        uri3 = daemon.register(p3)
        uri4 = daemon.register(p4)

        # Register names with the Name Server
        ns.register("laptop", uri1)
        ns.register("ram", uri2)
        ns.register("bag", uri3)
        ns.register("charger", uri4)

        print("Server is ready!")
        print("Registered products:")
        print("- laptop")
        print("- ram")
        print("- bag")
        print("- charger")

        # Keep server running for client requests
        daemon.requestLoop()

    except Exception as e:
        print("Server error:", e)


if __name__ == "__main__":
    main()
