function changeBackground() {
  const uploadInput = document.getElementById('uploadImg');
  const linkInput = document.getElementById('imgLink');
  const body = document.body;

  if (uploadInput.files && uploadInput.files[0]) {
    const file = uploadInput.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
      const imageData = e.target.result;
      localStorage.setItem('backgroundImage', imageData);
      setBackground(imageData);
    }

    reader.readAsDataURL(file);
  }
  else if (linkInput.value) {
    localStorage.setItem('backgroundImage', linkInput.value);
    setBackground(linkInput.value);
  }
  else {
    alert('Por favor, envie uma imagem ou um link válido.');
  }
}

function setBackground(imageUrl) {
  document.body.style.backgroundImage = `url(${imageUrl})`;
  document.body.style.backgroundSize = 'cover';
  document.body.style.backgroundPosition = 'center';
}

// Ao carregar a página, aplica o background salvo
window.onload = function() {
  const savedImage = localStorage.getItem('backgroundImage');
  if (savedImage) {
    setBackground(savedImage);
  }
}
