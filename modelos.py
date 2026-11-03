# Módulo de Modelos de Datos - Sistema de Gestión 'Software FJ'

from abc import ABC, abstractmethod

# 1. CLASE ABSTRACTA BASE

class EntidadBase(ABC):
  """Clase abstracta base para garantizar la identificacion de entidades."""
  
  def __init__(self, id_entidad):
        self._id_entidad = id_entidad  # Atributo protegido
    @property
  def id_entidad(self):
    return self._id_entidad
