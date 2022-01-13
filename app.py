from docarray import Document, DocumentArray
from jina import Flow

Document(text='hello, world.')

recipe1 = Document(text=input('Enter the recipe'))
recipe2 = Document(text='ravioli pasta')

recipe_collection = DocumentArray(recipe1, recipe2)
# da = DocumentArray(Document(text=s.strip()) for s in d.text.split('\n') if s.strip())
# da.apply(lambda d: d.embed_feature_hashing())

flow_index = (
    Flow()
    .add(
            uses="jinahub://PQLiteIndexer/v0.1.7",
            name="indexer",
            uses_with={
                'dim': DIMS,
                'columns': columns,
                # 'columns': COLUMNS,
                'metric': "cosine",
                'include_metadata': True
            }
)

with flow_index:
        flow_index.index(inputs=recipe_collection, show_progress=True)


def searchRecipe():
    flow_search = (
        Flow()
        .add(
            uses="jinahub://PQLiteIndexer/v0.1.7",
            name="indexer",
            uses_with={
                'dim': DIMS,
                'columns': columns,
                'metric': "cosine",
                'include_metadata': True
            },
            uses_metas={"workspace": WORKSPACE_DIR},
            volumes=f"./{WORKSPACE_DIR}:/workspace/workspace",
            install_requirements=True
        )
    )

    
