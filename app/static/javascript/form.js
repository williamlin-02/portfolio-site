const form = document.getElementById('form')

form.addEventListener('submit', function(e){
    e.preventDefault();
    
    const prePayload = new FormData(form);
    const payload = new URLSearchParams(prePayload);

    console.log([...payload])

    fetch('/api/timeline_post', {
        method: 'POST',
        body: payload,
    })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.log(err))

    form.reset();
})