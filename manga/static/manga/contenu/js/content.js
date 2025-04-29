// Debut du slide
// Declaration des variable
let btnSlide = document.querySelectorAll('.btnSlide');

// Function silde custom
let sildeCustom = (slide) => {
    if (slide) {
        // Garder une référence vers l'élément précédemment cliqué
        let elementPrecedent = null;
        for (let i = 0; i < slide.length; i++) {

            slide[i].addEventListener('click', function(event) {
                // Récupérer l'élément cliqué
                let elementClique = event.currentTarget.querySelector('img');
                // Recuperer le premier elements
                let premierelement = slide[0].querySelector('img');
                // Récupérer le href du premier élément
                let hrefPremierElement = premierelement.getAttribute('src');

                // Vérifier si l'élément n'est pas le premier dans la liste
                if (i !== 0) {
                    // Effectuer les actions nécessaires pour les éléments autres que le premier
                    if (event.target) {
                        event.target.classList.toggle('active_slide');
                        // Vérifiez si la classe existe sur cet élément
                        if (event.target.classList.contains('active_slide')) {
                            premierelement.setAttribute('src', `${event.target.getAttribute('src')}`)
                            event.target.setAttribute('src', `${hrefPremierElement}`);
                        } else {
                            premierelement.setAttribute('src', `${event.target.getAttribute('src')}`)
                            event.target.setAttribute('src', `${hrefPremierElement}`);
                        }
                        // console.log(event.target);
                        // console.log(premierelement);
                        // console.log(hrefPremierElement);
                        // console.log(event.target.getAttribute('src'));
                    }
                } else {
                    // Si c'est le premier élément, vous pouvez ignorer le clic ou effectuer d'autres actions
                    console.log('Clic sur le premier élément ignoré.');
                }
            });
        }
    }
}

sildeCustom(btnSlide)