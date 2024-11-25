const fileInput = document.getElementById('id_foto_perfil');
    const submitButton = document.getElementById('submit-button');

    fileInput.addEventListener('change', function() {
        if (fileInput.files.length > 0) {
            // Mostrar o botão se uma imagem for selecionada
            submitButton.style.display = 'inline-block';
        } else {
            // Ocultar o botão se nenhuma imagem estiver selecionada
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

    // Verifica se o arquivo foi selecionado
    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            // Atualiza a imagem ou adiciona a nova imagem no contêiner
            if (previewImage) {
                previewImage.src = e.target.result;
            } else {
                const img = document.createElement('img');
                img.id = 'preview-image';
                img.src = e.target.result;
                img.style.width = '100%';
                img.style.height = '100%';
                img.style.objectFit = 'cover';
                imageContainer.innerHTML = ''; // Remove o texto "Sem foto"
                imageContainer.appendChild(img);
            }
        };
        reader.readAsDataURL(fileInput.files[0]);
        // Exibe o botão de salvar/editar
        submitButton.style.display = 'block';
    } else {
        // Se nenhum arquivo for selecionado, restaura o estado inicial
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
    document.getElementById('popup').style.display = 'flex'; // Mostra o popup
}

function fecharPopup() {
    document.getElementById('popup').style.display = 'none'; // Esconde o popup
}
