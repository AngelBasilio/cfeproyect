// Función para cerrar la modal de duplicado y mostrar la modal de error general
function handleDuplicateClose() {
    document.getElementById('duplicateModal').classList.remove('active');
  
    // Si hay un error general, muestra la modal de error
    const errorModal = document.getElementById('errorModal');
    if (errorModal.classList.contains('active')) {
      errorModal.classList.add('active');
    }
  }
  
  // Inicializar estado de las modals
  window.onload = function () {
    const duplicateModal = document.getElementById('duplicateModal');
    const errorModal = document.getElementById('errorModal');
  
    // Si ambos errores están activos, mostrar solo la modal de duplicado
    if (duplicateModal.classList.contains('active') && errorModal.classList.contains('active')) {
      errorModal.classList.remove('active');
    }
  };

