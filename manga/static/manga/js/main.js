// Background du header lors du scroll Debut 
let header = (header) => {
    if (header) {
        let lastScrollPosition = window.pageYOffset; // Stocker la dernière position de défilement

        window.addEventListener('scroll', function() {
            const currentScrollPosition = window.pageYOffset; // Obtenir la position de défilement actuelle

            if (currentScrollPosition > lastScrollPosition) {
                document.getElementById('navbarprincipal').style.backgroundColor = '#000000c7';

            } else if (currentScrollPosition === 0) {
                document.getElementById('navbarprincipal').style.backgroundColor = 'transparent';
            } else {
                // console.log("L'utilisateur fait défiler vers le haut.");
            }

            lastScrollPosition = currentScrollPosition; // Mettre à jour la dernière position de défilement
        });

        document.querySelector('.btn-inscription').addEventListener('click', event => {
            // document.querySelector('');
        });
    }
}

header(document.getElementById('header'));
// Background du header lors du scroll Fin

let main = (main) => {
    if (main) {
        let content = ` `;
        main.innerHTML = content;
        // second page
        $('.your-class').slick({
            centerMode: true,
            centerPadding: '60px',
            slidesToShow: 3,
            responsive: [{
                    breakpoint: 768,
                    settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: '40px',
                        slidesToShow: 3
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: '40px',
                        slidesToShow: 1
                    }
                }
            ]
        });
    }
}

/*
/ le slider pour contenu la nav seconde 
pour la presentation des mangas, Anime, L-Novel
*/
// Debut slider

let slider_nav = (contentslider) => {

    // Sélectionnez le corps (body) de votre document HTML
    const body = contentslider;

    // Vérifiez si la classe existe dans le corps (body)
    if (body) {

        var swiper = new Swiper(".mySwiper", {
            slidesPerView: 3,
            spaceBetween: 30,
            freeMode: true,
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
            // autoplay: {
            //     delay: 5000,
            // },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },

        });

        // Sélectionnez tous les éléments de lien dans la barre de navigation
        const navLinks = document.querySelectorAll('#default-tab button');

        // Parcourez tous les liens
        navLinks.forEach(link => {
            // Ajoutez un écouteur d'événements de clic à chaque lien
            link.addEventListener('click', function() {
                // Supprimez la classe "active" de tous les liens
                navLinks.forEach(link => link.classList.remove('active'));
                // Ajoutez la classe "active" au lien cliqué
                this.classList.add('active');
            });
        });
    }
}
slider_nav(document.querySelector('.slider-container'));
// Fin slider

let hoverImage = (first) => {
    document.addEventListener("DOMContentLoaded", function() {

        if (first) {
            const firstImage = first;

            for (elements of firstImage) {
                elements.addEventListener("mouseover", function(event) {
                    let secondImage = event.srcElement;

                    secondImage.style.opacity = "1";
                });

                elements.addEventListener("mouseout", function(event) {
                    let secondImage = event.srcElement;
                    secondImage.style.opacity = "0";
                });
            }
        }
    });
}

hoverImage(document.querySelectorAll(".image-container"));

let button_nav_second = (btn_nav) => {
    if (btn_nav) {
        let btn = btn_nav;
        let contenus = document.querySelectorAll('.tab-content');
        let elementarray = [];

        for (let i = 0; i < btn.length; i++) {
            btn[i].addEventListener("click", function() {
                activerOnglet(i);
            });
        }

        function activerOnglet(index) {
            // Masquer tous les contenus
            for (let i = 0; i < contenus.length; i++) {
                contenus[i].style.display = "none";
            }

            // Afficher le contenu sélectionné
            contenus[index].style.display = "block";

            // Supprimer la classe "actif" de tous les btn
            for (let i = 0; i < btn.length; i++) {
                btn[i].classList.remove("actif");
            }

            // Ajouter la classe "actif" à l'onglet sélectionné
            btn[index].classList.add("actif");
        }

    }
}
button_nav_second(document.querySelectorAll('.btn-nav-second'));

let content_error = (labelerror) => {
    if (labelerror) {
        if (document.querySelector('.errorlist.nonfield')) {
            diverror = document.querySelector('.errorlist.nonfield');
            // Ajouter l'élément à la div cible en utilisant appendChild()
            labelerror.appendChild(diverror);
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');
    if (form) {
        alert()
        form.setAttribute('autocomplete', 'off');
        var inputs = form.querySelectorAll('input');
        inputs.forEach(function(input) {
            input.setAttribute('autocomplete', 'off');
        });
    }
});

content_error(document.querySelector('.content_error'));