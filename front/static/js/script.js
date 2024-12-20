// // Ajouter une nouvelle entrée (fonctionnalité fictive)
// document.getElementById("addButton").addEventListener("click", function() {
//     alert("Ajouter un nouvel abonné");
// });

// // Fonction pour modifier une entrée
// // function editEntry() {
// //     alert("Modifier cet abonné");
// // }

// // Fonction pour supprimer une entrée
// // function deleteEntry() {
// //     if (confirm("Voulez-vous vraiment supprimer cet abonné ?")) {
// //         alert("Abonné supprimé !");
// //     }
// // }


function openModal(nom, prenom, adresse, Date_dinscription, Liste_emprunts_cours, historique_emprunts) {
    // Ouvrir le modal
    document.getElementById('editModal').style.display = "block";

    // Remplir les champs du formulaire avec les données de l'abonné
    document.getElementById('nom').value = nom;
    document.getElementById('prenom').value = prenom;
    document.getElementById('adresse').value = adresse;
    document.getElementById('Date_dinscription').value = Date_dinscription;
    document.getElementById('Liste_emprunts_cours').value = Liste_emprunts_cours;
    document.getElementById('historique_emprunts').value = historique_emprunts;

    // Remplir un champ caché pour la soumission du formulaire
    document.getElementById('abonneNom').value = nom;
}

function closeModal() {
    // Fermer le modal
    document.getElementById('editModal').style.display = "none";
}

// Fermer le modal si l'utilisateur clique en dehors de la zone du modal
window.onclick = function(event) {
    if (event.target == document.getElementById('editModal')) {
        closeModal();
    }
}



//barre de rechrche abonne
document.getElementById('searchInput').addEventListener('input', function() {
    const filter = this.value.toLowerCase();
    const rows = document.querySelectorAll('#abonnesTable tr');

    rows.forEach(row => {
        const cells = Array.from(row.cells);
        const matches = cells.some(cell => cell.textContent.toLowerCase().includes(filter));
        row.style.display = matches ? '' : 'none';
    });
});

//barre de recherche livre
document.getElementById('searchInput').addEventListener('input', function() {
    const filter = this.value.toLowerCase();
    const rows = document.querySelectorAll('#livresTable tr');

    rows.forEach(row => {
        const cells = Array.from(row.cells);
        const matches = cells.some(cell => cell.textContent.toLowerCase().includes(filter));
        row.style.display = matches ? '' : 'none';
    });
});

//barre de recherche emprunt
document.getElementById('searchInput').addEventListener('input', function() {
    const filter = this.value.toLowerCase();
    const rows = document.querySelectorAll('#empruntsTable tr');

    rows.forEach(row => {
        const cells = Array.from(row.cells);
        const matches = cells.some(cell => cell.textContent.toLowerCase().includes(filter));
        row.style.display = matches ? '' : 'none';
    });
});


    // Lorsque le bouton de suppression est cliqué, on met à jour l'URL du formulaire
    const deleteButtons = document.querySelectorAll('.delete-btn');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const url = button.getAttribute('data-href');
            const deleteForm = document.getElementById('deleteForm');
            deleteForm.setAttribute('action', url);
        });
    });



