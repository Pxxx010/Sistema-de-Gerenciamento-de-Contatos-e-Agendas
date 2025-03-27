from mongoengine import Document, StringField, ListField, ReferenceField, connect

connect("contact_db")

class Contact(Document):
    name = StringField(required=True)
    phone = StringField(required=True)
    
class Agenda(Document):
    name = StringField(required=True)
    contacts = ListField(ReferenceField(Contact))
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save()
        print(f"Contato adicionado à agenda {self.name} com sucesso!")

def print_header():
    print("\n" + "="*50)
    print("SISTEMA DE GERENCIAMENTO DE CONTATOS E AGENDAS")
    print("="*50 + "\n")

def print_menu():
    print("\nMENU PRINCIPAL:")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Criar Agenda")
    print("4. Listar Agendas")
    print("5. Adicionar Contato à Agenda")
    print("6. Sair")
    print("-"*50)

def add_contact(name, phone, agenda_name=None):
    contact = Contact(name=name, phone=phone)
    contact.save()
    print(f"\n✓ Contato {name} salvo com sucesso!")
    
    if agenda_name:
        agenda = Agenda.objects(name=agenda_name).first()
        if agenda:
            agenda.add_contact(contact)
        else:
            print(f"❌ Agenda '{agenda_name}' não encontrada!")
    return contact

def list_contacts():
    contacts = Contact.objects()
    if not contacts:
        print("\n❌ Nenhum contato cadastrado!")
        return
        
    print("\nLISTA DE CONTATOS:")
    print("-"*30)
    for contact in contacts:
        print(f"📱 Nome: {contact.name}")
        print(f"📞 Telefone: {contact.phone}")
        print("-"*30)

def create_agenda(name):
    agenda = Agenda(name=name)
    agenda.save()
    print(f"\n✓ Agenda '{name}' criada com sucesso!")
    return agenda

def list_agendas():
    agendas = Agenda.objects()
    if not agendas:
        print("\n❌ Nenhuma agenda cadastrada!")
        return
        
    print("\nLISTA DE AGENDAS:")
    print("="*50)
    for agenda in agendas:
        print(f"\n📚 Agenda: {agenda.name}")
        print("-"*30)
        if agenda.contacts:
            print("Contatos:")
            for contact in agenda.contacts:
                print(f"  • {contact.name} - {contact.phone}")
        else:
            print("  (Nenhum contato cadastrado)")
        print("-"*30)

def add_contact_to_agenda(agenda_name, contact_name):
    agenda = Agenda.objects(name=agenda_name).first()
    contact = Contact.objects(name=contact_name).first()
    
    if agenda and contact:
        agenda.add_contact(contact)
    else:
        print("\n❌ Agenda ou contato não encontrado!")

if __name__ == "__main__":
    print_header()
    
    while True:
        print_menu()
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            print("\nADICIONAR CONTATO")
            print("-"*30)
            name = input("Nome: ")
            phone = input("Telefone: ")
            
            add_to_agenda = input("\nDeseja adicionar a uma agenda? (s/n): ").lower()
            if add_to_agenda == 's':
                agenda_name = input("Nome da agenda: ")
                add_contact(name, phone, agenda_name)
            else:
                add_contact(name, phone)
                
        elif opcao == "2":
            list_contacts()
            
        elif opcao == "3":
            print("\nCRIAR NOVA AGENDA")
            print("-"*30)
            name = input("Nome da agenda: ")
            create_agenda(name)
            
        elif opcao == "4":
            list_agendas()
            
        elif opcao == "5":
            print("\nADICIONAR CONTATO À AGENDA")
            print("-"*30)
            agenda_name = input("Nome da agenda: ")
            contact_name = input("Nome do contato: ")
            add_contact_to_agenda(agenda_name, contact_name)
            
        elif opcao == "6":
            print("\nObrigado por usar o sistema!")
            break
            
        else:
            print("\n❌ Opção inválida!")
