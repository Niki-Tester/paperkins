const removeImage = document.getElementsByClassName('remove-image');
for (const image of removeImage) {
	image.addEventListener('click', handleRemoveImage);
}

async function handleRemoveImage(e) {
	const imageId = e.currentTarget.dataset.imageId;
	const response = await fetch('/products/remove_image/', {
		method: 'DELETE',
		cache: 'no-cache',
		headers: {
			'content-type': 'application/json',
		},
		body: JSON.stringify({image_id: imageId}),
	});

	if (response.status === 200) {
		const removedImage = e.target.parentElement;
		removedImage.remove();
	}
}
