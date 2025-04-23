import tkinter as tk
from tkinter import filedialog, ttk, colorchooser, font, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from pypdf import PdfWriter
import os

class SimplePDFMergeApp(TkinterDnD.Tk): # Inherit from TkinterDnD.Tk for drag and drop
    def __init__(self):
        super().__init__()

        # --- Window Configuration ---
        self.title("Simple PDF Editor") # Using the requested title
        self.geometry("800x600")

        # --- Styling ---
        self.style = ttk.Style(self)

        # Define colors (hardcoded dark theme)
        self.interface_bg = "#367588" # Blue Teal
        self.drop_box_bg = "#0a7e8c" # Metallic Seaweed
        self.text_color = "black" # Text color
        self.button_bg_normal = "#4a148c" # Dark Purple
        self.button_fg_normal = "#4c516d" # Independence
        self.button_bg_hover = "#7b1fa2" # Light Purple
        self.button_fg_hover = "black"

        # Define font
        self.text_font = font.Font(family="Verdana", size=12)

        # Configure styles
        self.style.configure("TLabel", font=self.text_font, foreground=self.text_color)  # Set default text color
        self.style.configure("TButton", font=self.text_font, padding=5, relief="raised",  # Set relief to raised
                             background=self.button_bg_normal, foreground=self.button_fg_normal)  # Set normal colors

        # Configure button colors on hover state
        self.style.map("TButton",
                       background=[('active', self.button_bg_hover), ('!active', self.button_bg_normal)],
                       foreground=[('active', self.button_fg_hover), ('!active', self.button_fg_normal)])

        # Configure frame background color
        self.style.configure("TFrame", background=self.interface_bg)
        self.style.configure("TLabelframe", background=self.interface_bg)  # Although no labelframe here, good practice

        # Apply interface background to the root window
        self.configure(bg=self.interface_bg)

        # --- Menu Bar ---
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        self.about_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="About", menu=self.about_menu)
        self.about_menu.add_command(label="About this application", command=self.show_about)

        # --- Main Frame for Merging ---
        self.main_frame = ttk.Frame(self, padding="10")
        self.main_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(2, weight=2)  # Give weight to the listbox row

        # --- Drop Box Area ---
        self.drop_frame = ttk.Frame(self.main_frame, padding="20")
        self.drop_frame.grid(row=0, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        # Configure grid within the drop_frame for side-by-side layout
        self.drop_frame.columnconfigure(0, weight=1)  # Give weight to the column containing the label
        self.drop_frame.columnconfigure(1, weight=1)  # Give weight to the column containing the button
        self.drop_frame.rowconfigure(0, weight=1)  # Give weight to the row containing both

        # Apply the lighter background to the drop frame
        self.style.configure("DropBox.TFrame", background=self.drop_box_bg)
        self.drop_frame.configure(style="DropBox.TFrame")

        self.drop_label = ttk.Label(self.drop_frame, text="Drag and drop PDF files here")
        # Use pack or grid within the drop_frame as needed
        self.drop_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

        self.select_files_button_in_drop = ttk.Button(self.drop_frame, text="Select PDF files",
                                                      command=self.select_pdf_files_for_merge)
        # Use sticky="w" to stick to the west side of its cell
        self.select_files_button_in_drop.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Configure drag and drop specifically for the drop frame
        self.drop_frame.drop_target_register(DND_FILES)
        self.drop_frame.dnd_bind('<<Drop>>', self.drop_files_for_merge)

        # --- File List Display ---
        self.file_list_label = ttk.Label(self.main_frame, text="Files to Merge:")
        self.file_list_label.grid(row=1, column=0, sticky=tk.W, pady=5)

        self.file_listbox = tk.Listbox(self.main_frame, width=100, height=10, font=self.text_font)
        self.file_listbox.grid(row=2, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        # Apply colors to listbox manually as ttk styles don't fully control it
        self.file_listbox.configure(bg=self.drop_box_bg, fg=self.text_color)

        # --- Control Buttons ---
        self.remove_button = ttk.Button(self.main_frame, text="Remove Selected",
                                        command=self.remove_selected_merge_files)
        self.remove_button.grid(row=3, column=0, sticky=tk.W, pady=10)

        self.merge_button = ttk.Button(self.main_frame, text="Merge PDFs", command=self.perform_merge)
        self.merge_button.grid(row=3, column=1, sticky=tk.E, pady=10)

        # --- File List for Merging ---
        self.pdf_files_to_merge = []  # List to store paths of files to merge

    def show_about(self):
        messagebox.showinfo(
            "About Simple PDF Merger",
            "Simple PDF Merger\n\n"
            "Version: 1.0\n"  # Placeholder version
            "Contact: svanbuggenum@gmail.com\n"
            "Website: www.svanbuggenumanalytics.com"
            "GitHub: https://github.com/SnowY4you"
        )

    def select_pdf_files_for_merge(self):
        files = filedialog.askopenfilenames(
            title="Select PDF Files to Merge",
            filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
        )
        if files:
            for file in files:
                if file not in self.pdf_files_to_merge:
                    self.pdf_files_to_merge.append(file)
                    self.file_listbox.insert(tk.END, os.path.basename(file))

    def drop_files_for_merge(self, event):
        files = self.root.tk.splitlist(event.data)
        for file in files:
            # Clean up path format from drag-and-drop if necessary (e.g., remove curly braces)
            file = file.strip('{}')
            if file.lower().endswith('.pdf') and file not in self.pdf_files_to_merge:
                self.pdf_files_to_merge.append(file)
                self.file_listbox.insert(tk.END, os.path.basename(file))

    def remove_selected_merge_files(self):
        selected_indices = self.file_listbox.curselection()
        for index in reversed(selected_indices):
            self.file_listbox.delete(index)
            del self.pdf_files_to_merge[index]

    def perform_merge(self):
        if not self.pdf_files_to_merge:
            messagebox.showwarning("Warning", "Please select PDF files to merge.")
            return

        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")),
            title="Save Merged PDF As"
        )

        if not output_path:
            return  # User cancelled save

        merger = PdfWriter()
        try:
            for pdf_path in self.pdf_files_to_merge:
                merger.append(pdf_path)
            merger.write(output_path)
            messagebox.showinfo("Success", f"PDFs merged successfully to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during merging: {e}")
        finally:
            merger.close()

if __name__ == "__main__":
    app = SimplePDFMergeApp()
    app.mainloop()
