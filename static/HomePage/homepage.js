const uploadfile = document.getElementById('imagechooser');
const previewimg = document.getElementById('imagepreview');
const postcreationmenu = document.getElementById('go-to-post-creation');
const postmenu = document.querySelector('.post-creation-container');
const closepostcreation = document.getElementById('close-postcreation');
const submitpost = document.getElementById('submitbtn');

uploadfile.addEventListener('change', function() {

    const file = this.files[0];

    if (file) {
        const objectURL = URL.createObjectURL(file);

        previewimg.src = objectURL;

        previewimg.style.display = 'block';
    }
});

postcreationmenu.addEventListener('click', function() {
    postmenu.style.display = 'flex';
});

closepostcreation.addEventListener('click', function() {
    postmenu.style.display = 'none';
});

submitpost.addEventListener('click', function() {
    postmenu.style.display = 'none';
});