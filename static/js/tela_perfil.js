// PERSONALIZAÇÕES PARA FOTO E BOTÃO
const fileInput = document.getElementById('id_foto_perfil');
    const submitButton = document.getElementById('submit-button');

    fileInput.addEventListener('change', function() {
        if (fileInput.files.length > 0) {
            
            submitButton.style.display = 'inline-block';
        } else {
            
            submitButton.style.display = 'none';
        }
    });

//pré visualização da foto
function previewImage() {
    const fileInput = document.getElementById('id_foto_perfil');
    const imageContainer = document.getElementById('image-container');
    const previewImage = document.getElementById('preview-image');
    const noPhotoText = document.getElementById('no-photo-text');
    const submitButton = document.getElementById('submit-button');

    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
        
            if (previewImage) {
                previewImage.src = e.target.result;
            } else {
                const img = document.createElement('img');
                img.id = 'preview-image';
                img.src = e.target.result;
                img.style.width = '100%';
                img.style.height = '100%';
                img.style.objectFit = 'cover';
                imageContainer.innerHTML = ''; 
                imageContainer.appendChild(img);
            }
        };
        reader.readAsDataURL(fileInput.files[0]);
        
        submitButton.style.display = 'block';
    } else {
        
        if (previewImage) {
            previewImage.remove();
        }
        if (noPhotoText) {
            noPhotoText.style.display = 'block';
        }
        submitButton.style.display = 'none';
    }
}

//POPUP DAS DOAÇÕES
function mostrarDetalhes() {
    document.getElementById('popup').style.display = 'flex'; 
}

function fecharPopup() {
    document.getElementById('popup').style.display = 'none'; 
}
