class SingleLinkedList: 

    class Node: 
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_node(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def push_head_node(self, value):
        new_node = self.Node(value)
        if self.tail == None and self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def show_info_sll(self):
        print_sll = []
        current_node = self.head

        while current_node != None: 
            print_sll.append(current_node.value)
            current_node = current_node.next

        print(f'lista actual: {print_sll} \n cantidad de nodos {self.length}' )

    def shift_head_node(self):
        if self.length == 0:  #Verificamos que no haya nada en la lista
            self.head = None
            self.tail = None 
        else: 
            remove_node = self.head #Actualizamos el nombre de la cabeza con la variable auxiliar
            self.head = remove_node.next  #Actualizamos la cabeza de la lista
            remove_node.next = None #Eliminamos el enlace de remove_node con la lista
        self.length-=1

    def pop_node(self):
        if self.length == 0:  #Verificamos que no haya nada en la lista
            self.head = None
            self.tail = None 
        else: 
            current_node = self.head
            ahora = current_node

            while current_node.next != None: 
                ahora = current_node
                current_node = current_node.next
            
            self.tail = ahora
            self.tail.next = None
            self.length-=1

    def get_node(self, index):
        if index > 1 and index < self.length:
            contador = 1
            current_node = self.head

            while contador < self.length and contador < index:
                contador += 1
                current_node = current_node.next

            return current_node
        elif index == self.length:
            return self.tail
        elif index == 1: 
            return self.head
        else: 
            return None

    def get_node_value(self, index):
        if index > 1 and index < self.length:
            contador = 1
            current_node = self.head

            while contador < self.length and contador < index:
                contador += 1
                current_node = current_node.next

            return current_node.value
        elif index == self.length:
            return self.tail.value
        elif index == 1: 
            return self.head.value
        else: 
            return None

    def update_node_value(self, index, value):
       search_node = self.get_node(index)
       if search_node != None: 
        search_node.value = value #encontró el nodo y se puede actualizar
        return search_node.value
       else: 
        print('No se encontró el nodo a buscar')
        return None 
    
    def remove_node(self, index): 
        if index == 1: 
            self.shift_head_node()
        elif index == self.length:
            self.pop_node()
        else: 
            remove_node = self.get_node(index)
            if remove_node != None:
                previous_node = self.get_node(index - 1)
                previous_node.next = remove_node.next
                remove_node.next = None
            self.length-=1
    



            
