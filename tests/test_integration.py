from src.models import Apartment
from src.manager import Manager
from src.models import Parameters


def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key

def test_tenants_in_manager():
    parameters = Parameters()
    manager = Manager(parameters)
    assert len(manager.tenants) > 0
    names = [tenant.name for tenant in manager.tenants.values()]
    for tenant in ['Jan Nowak', 'Adam Kowalski', 'Ewa Adamska']:
        assert tenant in names

def test_if_tenants_have_valid_apartment_keys():
    parameters = Parameters()
    manager = Manager(parameters)
    assert manager.check_tenants_apartment_keys() == True

    manager.tenants['tenant-1'].apartment = 'invalid-key'
    assert manager.check_tenants_apartment_keys() == False

def test_apartment_cost():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.bills, list) #czy bills jest listą
    assert manager.get_apartment_costs("apart-polanka", "2025", "02")==910.0 #poprawne obliczenie dla apart-polanka w 02.2025
    assert manager.get_apartment_costs("nie_istnieje", "2025", "02")==None #nie ma apartamentu w bazie
    assert manager.get_apartment_costs("apart-polanka", "2025", "01")==0.0 #apartament istnieje, brak rachunków w miesiącu