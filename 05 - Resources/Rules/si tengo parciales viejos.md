Handling raw media like 10 separate JPGs of old exams is a classic Zettelkasten challenge. If you just drop those images directly into your `02 - Reference Notes` folder, you will instantly recreate the clutter you are trying to escape.

In Obsidian, the best practice is to separate the **raw file** from the **contextual note**. Here is the exact workflow to manage those exam photos cleanly:

### 1. Set Up an Attachments Vault (The Storage)

Your raw JPGs, PDFs, and screenshots should not live in your main knowledge folders.

- Create a new folder at the root of your vault called `99 - Attachments` (or `Assets`).
    
- Go to Obsidian **Settings > Files and Links**.
    
- Change the **"Default location for new attachments"** to this new folder.
    
    Now, whenever you paste or drag an image into Obsidian, it gets hidden away in this folder automatically, keeping your Zettelkasten completely clean.
    

### 2. Create a "Wrapper" Reference Note

Instead of having 10 loose files, you will create **one** single Markdown file in `02 - Reference Notes` to act as the container for all those images.

- **Naming Convention:** Name it something like `REF - Exam - DSI - Parciales Viejos 2023`.
    
- **Properties:** Add your standard YAML frontmatter so Dataview can find it:
    
    YAML
    
    ```
    ---
    subject: "DSI"
    exam: "Parcial 1"
    zk_type: "reference"
    status: "to_process"
    ---
    ```
    

### 3. Embed and Structure the Images

Open your new `REF` note and drag the 10 JPGs directly into it. Obsidian will automatically save the raw files in your Attachments folder and generate embed links (e.g., `![[parcial_1_page1.jpg]]`) inside the note.

- Add markdown headers above the images to give them structure, like `### Parcial 2023 - Turno Mañana` or `### Tema A`.
    

### The Zettelkasten Workflow for Exams

When it is time to study, you don't just stare at the images. You process them.

If you notice that a specific question about GRASP patterns or SOLID principles appears in three different old exams, you extract that concept. You create a new Permanent Note (e.g., `High Cohesion Principle`), write the answer in your own words, and in the `source` property of that permanent note, you link back to your `[[REF - Exam - DSI - Parciales Viejos 2023]]`.

This ensures your database remains text-first and highly searchable, while the heavy images are neatly organized in a single accessible hub.

Do you already have an attachments folder configured in your Obsidian settings, or do we need to set that up before you start dragging those exam photos in?