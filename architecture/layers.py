class L1Provider:
    def l1_service(self):
        raise NotImplementedError("Subclasses should implement this!")


class L2Provider:
    def __init__(self):
        self.level1 = None

    def l2_service(self):
        raise NotImplementedError("Subclasses should implement this!")

    def set_lower_layer(self, l1):
        self.level1 = l1


class L3Provider:
    def __init__(self):
        self.level2 = None

    def l3_service(self):
        raise NotImplementedError("Subclasses should implement this!")

    def set_lower_layer(self, l2):
        self.level2 = l2


class DataLink(L1Provider):
    def l1_service(self):
        print("L1Service doing its job")


class Transport(L2Provider):
    def l2_service(self):
        print("L2Service starting its job")
        if self.level1:
            self.level1.l1_service()
        print("L2Service finishing its job")


class Session(L3Provider):
    def l3_service(self):
        print("L3Service starting its job")
        if self.level2:
            self.level2.l2_service()
        print("L3Service finishing its job")


if __name__ == "__main__":
    datalink = DataLink()
    transport = Transport()
    session = Session()

    transport.set_lower_layer(datalink)
    session.set_lower_layer(transport)

    session.l3_service()
