const topics = [
    { name: "Dashboard", iconClass: "bi bi-houses-fill", link: "#", page: "Dashboard" },
    { name: "Pagamento", iconClass: "bi bi-credit-card-2-front-fill", link: "#", page: "Pagamento" },
    { name: "Relatórios", iconClass: "bi bi-bar-chart-line-fill", link: "#", page: "Relatórios" }

];
  
function createNavItem(topic) {
    const li = document.createElement("li");
    li.classList.add("nav-item");
  
    const a = document.createElement("a");
    a.classList.add("nav-link");
    a.href = topic.link;
    a.setAttribute("data-page", topic.page);
  
    const divIcon = document.createElement("div");
    divIcon.classList.add("icon", "icon-shape", "icon-sm", "shadow", "border-radius-md", "bg-white", "text-center", "me-2", "d-flex", "align-items-center", "justify-content-center", "opacity-9");
  
    const iIcon = document.createElement("i");
    iIcon.className = topic.iconClass; 
    iIcon.style.fontSize = "1rem";
    iIcon.style.color = "#141727"
  
    divIcon.appendChild(iIcon);
    a.appendChild(divIcon);
  
    const span = document.createElement("span");
    span.classList.add("nav-link-text", "ms-1");
    span.textContent = topic.name;
  
    a.appendChild(span);
    li.appendChild(a);
  
    return li;
}
  
function initializeSidebar() {
    const navList = document.getElementById("nav-list");
  
    topics.forEach(topic => {
      const navItem = createNavItem(topic);
      navList.appendChild(navItem);
    });
}
  
document.addEventListener("DOMContentLoaded", initializeSidebar);
  