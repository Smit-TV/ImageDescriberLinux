import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import configController

# Settings of Image Describer
class SettingsWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_default_size(300, 400)
        self.set_title("Image Describer")
        box = Gtk.Box()
        self.add(box)
        self.connect("destroy", Gtk.main_quit)
        inputBox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        box.pack_start(inputBox, False, False, 0)

        grokAPIKeyEntry = Gtk.Entry()
        grokAPIKeyEntry.set_text(configController.get_api_key())
        saveAPIKey = Gtk.Button(label = "Сохранить")
        grokAPIKeyLabel = Gtk.Label()
        grokAPIKeyLabel.set_label("Введите API-КЛЮЧ Grok:")
        grokAPIKeyLabel.set_mnemonic_widget(grokAPIKeyEntry)

        def on_save_clicked(_):
            key = grokAPIKeyEntry.get_text().strip()
            if len(key) == 0:
                return
            else:
                    configController.save_api_key(key)

        saveAPIKey.connect("clicked", on_save_clicked)

        inputBox.pack_start(grokAPIKeyLabel, False, False, 0)

        inputBox.pack_start(grokAPIKeyEntry, False, False, 0)
        inputBox.pack_start(saveAPIKey, False, False, 0)

        models = ["meta-llama/llama-4-scout-17b-16e-instruct", "meta-llama/llama-4-maverick-17b-128e-instruct"]
        selectedModel = configController.get_selected_model()
        selectedModelPosition = 0 if not selectedModel in models else models.index(selectedModel)
        modelSelector = Gtk.ComboBoxText()
        for model in models:
            modelSelector.append_text(model)
        modelSelector.set_active(selectedModelPosition)

        def on_model_selected(combo):
            model = combo.get_active_text()
            configController.save_model(model)

        modelSelector.connect("changed", on_model_selected)
        modelBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 6)
        box.pack_start(modelBox, False, False, 0)

        modelLabel = Gtk.Label()
        modelLabel.set_label("Модель Grok:")
        modelLabel.set_mnemonic_widget(modelSelector)
        modelBox.pack_start(modelLabel, False, False, 0)
        modelBox.pack_start(modelSelector, False, False, 0)

        instructions = Gtk.Entry()
        instructions.set_text(configController.get_instructions())
        instructionsBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 6)
        instructionsLabel = Gtk.Label()
        instructionsLabel.set_text("Введите инструкции для описания изображения:")
        instructionsLabel.set_mnemonic_widget(instructions)
        instructionsBox.pack_start(instructionsLabel, False, False, 0)
        instructionsBox.pack_start(instructions, False, False, 0)
        box.pack_start(instructionsBox, False, False, 0)
        saveInstructions = Gtk.Button()
        saveInstructions.set_label("Сохранить")

        def on_save_instructions(btn):
            text = instructions.get_text().strip()
            if len(text) == 0:
                return
            else:
                configController.save_instructions(text)

        saveInstructions.connect("clicked", on_save_instructions)
        instructionsBox.pack_start(saveInstructions, False, False, 0)

        close = Gtk.Button()
        close.set_label("Закрыть")
        close.connect("clicked", lambda btn: Gtk.main_quit())
        box.pack_start(close, False, False, 0)

    def main(self):
        Gtk.main()

