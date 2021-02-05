from faker import Faker

import faker_microservice

fake = Faker()
fake.add_provider(faker_microservice.Provider)
print(fake.microservice())  # prints "fulfilment_manager" or similar