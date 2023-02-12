const imageSelector = document.getElementById('image-selector');
const form = document.getElementById('product-form');
const hiddenInput = document.getElementById('primary-image-input');
const newImagesSection = document.getElementById('new-images');

document.getElementById('new-image').addEventListener('change', displayThumbnails);
form.addEventListener('submit', formSubmit);

function displayThumbnails(e) {
	const imageFiles = e.target.files;
	imageSelector.innerHTML = '';

	if (imageFiles.length > 0) {
		createImageSelectorElements(imageFiles);
		newImagesSection.style.display = 'block';
	} else {
		newImagesSection.style.display = 'none';
	}
}

const createImageSelectorElements = imageFiles => {
	for (const file of imageFiles) {
		const div = createDivElement();
		const img = createImageElement(file);

		div.appendChild(img);
		imageSelector.appendChild(div);

		addImageSelectionListeners(img);
	}
};

const displayErrorMessage = error => {
	document.getElementById('error-message').innerText = error;
};

const createImageElement = file => {
	const img = new Image();
	img.setAttribute('class', 'mt-1 border border-light image-thumbnail');
	img.src = URL.createObjectURL(file);
	img.setAttribute('data-file-name', file.name);
	return img;
};

const createDivElement = () => {
	const div = document.createElement('div');
	div.setAttribute('class', 'col-12 col-sm-6 col-lg-4 image-preview mb-2');
	return div;
};

const addImageSelectionListeners = img => {
	if (img) return img.addEventListener('click', setPrimaryImage);

	const images = document.getElementsByClassName('image-thumbnail');
	for (let i = 0; i < images.length; i++) {
		images[i].addEventListener('click', setPrimaryImage);
	}
};

const setPrimaryImage = e => {
	if (e.currentTarget.id === 'primary-image') {
		e.currentTarget.id = '';
		displayErrorMessage('');
		hiddenInput.setAttribute('value', '');
		return;
	}

	const imageThumbnails = document.getElementsByClassName('image-thumbnail');

	for (let i = 0; i < imageThumbnails.length; i++) {
		imageThumbnails[i].removeAttribute('id');
	}
	e.target.id = 'primary-image';
	hiddenInput.setAttribute('value', e.currentTarget.dataset.fileName);
};

function formSubmit(e) {
	form.reportValidity();
	const primaryImage = document.getElementById('primary-image');
	const imageThumbnails = document.getElementsByClassName('image-thumbnail');
	if (!primaryImage && imageThumbnails.length > 0) {
		e.preventDefault();
		displayErrorMessage('Error: Please select a Primary Image');
		return;
	}
	form.submit();
}

document.addEventListener('DOMContentLoaded', () => {
	addImageSelectionListeners();
	const primaryImage = document.getElementById('primary-image');
	if (!primaryImage) return;
	hiddenInput.defaultValue = primaryImage.dataset.fileName;
});
