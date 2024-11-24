// Ajouter une nouvelle entrée (fonctionnalité fictive)
document.getElementById("addButton").addEventListener("click", function() {
    alert("Ajouter un nouvel abonné");
});

// Fonction pour modifier une entrée
function editEntry() {
    alert("Modifier cet abonné");
}

// Fonction pour supprimer une entrée
function deleteEntry() {
    if (confirm("Voulez-vous vraiment supprimer cet abonné ?")) {
        alert("Abonné supprimé !");
    }
}
