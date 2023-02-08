const imagesInput = document.getElementById('new-image');

imagesInput.addEventListener('change', e =>{
  if (e.target.files.length <= 0) document.getElementById('filename').innerText = '';

  const imageSelector = document.getElementById('image-selector')
  imageSelector.innerHTML = '';

  const imageFiles = [];

  for (let i = 0; i < e.target.files.length; i++) {
    const file = e.target.files[i];
    imageFiles.push(file[i])
    const div = document.createElement('div')
    div.setAttribute('class', 'col-sm image-preview')
    
    const img = new Image();
    img.setAttribute('height', 139);
    img.setAttribute('width', 139);
    img.setAttribute('class', 'mt-1 border border-light preview-image');
    img.src = URL.createObjectURL(file);
    img.setAttribute('data-file-name', file.name)

    div.appendChild(img);
    imageSelector.appendChild(div);

    if(e.target.files.length == 1) {
      img.setAttribute('id', 'default-image');
      document.getElementById('filename').innerText = 'Default Image: ' + img.dataset.fileName;
    } else { 
      img.addEventListener('click', e =>{
        const previewImages = document.getElementsByClassName('preview-image')
        for (let i = 0; i < previewImages.length; i++) {
          previewImages[i].removeAttribute('id');
        }
        e.currentTarget.id = 'default-image';
        
        document.getElementById('filename').innerText = 'Default Image: ' + e.currentTarget.dataset.fileName;
      })
    }
  }
})