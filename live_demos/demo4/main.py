from taipy.gui import Gui
from main_module.page1 import page as page1
from main_module.page2 import page as page2

x = 0

y = 10

gui = Gui(page="<|navbar|>")
gui.add_page("page1", page1)
gui.add_page("page2", page2)
gui.run(run_browser=False)
