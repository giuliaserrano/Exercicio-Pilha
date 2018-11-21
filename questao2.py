class Pilha(): 
  def __init__(self):
    self.lista= []

  def push(self, item ):
    if not (self.AlreadyHas(item)):
      self.pilha.append(item)
  def AlreadyHas(self, item):
    return item in self.lista
