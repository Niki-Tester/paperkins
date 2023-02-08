const fileName = document.getElementById('file-name');
const imageSelector = document.getElementById('image-selector');
const form = document.getElementById('add-product-form');
const hiddenInput = document.getElementById('primary-image-input');

document.getElementById('new-image').addEventListener('change', displayThumbnails);
form.addEventListener('submit', formSubmit);

function displayThumbnails(e) {
	const imageFiles = e.target.files;

	setFileNameText('');
	setImageSelectorHTML('');

	imageFiles.length <= 0 ? (fileName.innerText = '') : createImageSelectorElements(imageFiles);
}

const createImageSelectorElements = imageFiles => {
	for (const file of imageFiles) {
		const div = createDivElement();
		const img = createImageElement(file);

		div.appendChild(img);
		imageSelector.appendChild(div);

		imageFiles.length == 1 ? setSingleImageAttributes(img, file) : addImageSelectionListener(img);
	}
};

const setFileNameText = text => {
	document.getElementById('filename').innerText = text;
};

const setImageSelectorHTML = html => {
	imageSelector.html = html;
};

const createImageElement = file => {
	const img = new Image();
	img.setAttribute('height', 139);
	img.setAttribute('width', 139);
	img.setAttribute('class', 'mt-1 border border-light image-thumbnail');
	img.src = URL.createObjectURL(file);
	img.setAttribute('data-file-name', file.name);
	return img;
};

const createDivElement = () => {
	const div = document.createElement('div');
	div.setAttribute('class', 'col-sm image-preview');
	return div;
};

const setSingleImageAttributes = (img, file) => {
	img.setAttribute('id', 'primary-image');
	setFileNameText('Default Image: ' + file.name);
	hiddenInput.setAttribute('value', file.name);
};

const addImageSelectionListener = img => {
	img.addEventListener('click', e => {
		const imageThumbnail = document.getElementsByClassName('image-thumbnail');
		for (let i = 0; i < imageThumbnail.length; i++) {
			imageThumbnail[i].removeAttribute('id');
		}
		e.currentTarget.id = 'primary-image';

		setFileNameText('Default Image: ' + e.currentTarget.dataset.fileName);
		hiddenInput.setAttribute('value', e.currentTarget.dataset.fileName);
	});
};

function formSubmit(e) {
	form.reportValidity();
	if (!document.getElementById('primary-image')) {
		e.preventDefault();
		setFileNameText('You need to select your primary image, before adding your new product');
		return;
	}
	form.submit();
}
