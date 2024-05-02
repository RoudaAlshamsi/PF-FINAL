class Supplier:
    def __init__(self, supplier_id, service):
        self.supplier_id = supplier_id
        self.service = service

    def updateService(self, newService):
        self.service = newService

    def get_SupplierID(self):
        return self.supplierID

    def get_service(self):
        return self.service
