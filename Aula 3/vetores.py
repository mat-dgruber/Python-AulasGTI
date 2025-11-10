import math

class Vetor2D:
  """
  Representa um vetor 2D (x, y) com componentes inteiros e
  operações de adição, subtração, multiplicação e divisão.
  """

  # 2. Inicializador (Construtor)
  def __init__(self, x, y):
    # Requisito 4: Armazena apenas valores inteiros
    if not (isinstance(x, int) and isinstance(y, int)):
      raise TypeError("Componentes X e Y devem ser inteiros")
    self.x = x
    self.y = y

  # 3. Representação (Requisito 6)
  def __repr__(self):
    """Retorna a representação oficial do objeto."""

    return f"Vetor2D(x={self.x}, y={self.y})"
  
  def __str__(self):
    """Retorna a representação "amigável" (string)."""

    return f"({self.x}, {self.y})"

  # 4. Método "Helper" para lidar com diferentes tipos (Requisito 5)
  def _normalize_other(self, other):
    """
    Valida e extrai os componentes (x, y) de 'other'.
    'other' pode ser um Vetor2D, um int ou uma tupla.
    """
    if isinstance(other, Vetor2D):
      return other.x, other.y
    elif isinstance(other, int):
      # Um inteiro é aplicado a ambos os componentes
      return other, other
    elif isinstance(other, tuple) and len(other) == 2:
      # Uma tupla deve conter dois inteiros
      if not (isinstance(other[0], int) and isinstance(other[1], int)):
        raise TypeError("Tupla deve conter dois inteiros para operar com Vetor2D")
      return other[0], other[1]
    
    # Se o tipo não for suportado, levantamos um TypeError
    # que será capturado pelos métodos de operação.
    raise TypeError(f"Operação com {type(other)} não suportada")

  # 5. Sobrecarga de Operadores (Requisito 3)
  
  def __add__(self, other):
    """Sobrecarga do operador de Adição (+)"""
    final = [0,0]
    if isinstance(other, Vetor2D):
      final = [other.x + other.y]
      
    try:
      other_x, other_y = self._normalize_other(other)
      return Vetor2D(self.x + other_x, self.y + other_y)
    except TypeError:
      return NotImplemented

  def __sub__(self, other):
    """Sobrecarga do operador de Subtração (-)"""
    try:
      other_x, other_y = self._normalize_other(other)
      return Vetor2D(self.x - other_x, self.y - other_y)
    except TypeError:
      return NotImplemented

  def __mul__(self, other):
    """Sobrecarga do operador de Multiplicação (*)"""
    try:
      other_x, other_y = self._normalize_other(other)
      return Vetor2D(self.x * other_x, self.y * other_y)
    except TypeError:
      return NotImplemented

  def __floordiv__(self, other):
    """
    Sobrecarga do operador de Divisão Inteira (//).
    Usamos // para garantir que o resultado seja inteiro (Req 4).
    """
    try:
      other_x, other_y = self._normalize_other(other)
      
      # Requisito 8: Checagem de divisão por zero
      if other_x == 0 or other_y == 0:
        raise DivisaoPorZeroVetorError("Divisão por zero em um componente do vetor")
        
      return Vetor2D(self.x // other_x, self.y // other_y)
    except TypeError:
      return NotImplemented