from functions import scrap_theblock, scrap_coindesk

route_table = [
    {"site_name": "theblock", "url": "https://www.theblock.co/latest"},
    {"site_name": "coindesk", "url": "https://www.coindesk.com/livewire/"},
]

site_funcs = {
    "theblock": scrap_theblock,
    "coindesk": scrap_coindesk,
}
