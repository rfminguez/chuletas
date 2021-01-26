function salutations() {
	let heading = document.querySelector('h1');
	if (heading.innerHTML === 'Hello') {
		heading.innerHTML='Goodbye!';
	} else {
		heading.innerHTML='Hello';
	}
}

// IMPORTANT: wait for the content of the DOM to be loaded 
document.addEventListener('DOMContentLoaded', function(){
	document.querySelector('button').onclick = salutations; 
});

