from app.retrieval import search_hybrid


def make_page(page_id: str, page_number: int) -> dict:
    return {
        "page_id": page_id,
        "document_id": "doc-a",
        "lecture": 1,
        "document_title": "Document A",
        "section": "section",
        "title": page_id,
        "page": page_number,
        "content": f"{page_id} content",
    }


def test_hybrid_combines_vector_neighbor_and_graph(monkeypatch):
    pages = [
        make_page("doc-a-p001", 1),
        make_page("doc-a-p002", 2),
        make_page("doc-a-p003", 3),
        make_page("doc-a-p004", 4),
    ]
    vector_hits = [
        {**pages[1], "distance": 0.1},
    ]
    graph_result = {
        "seeds": [
            {
                **pages[1],
                "distance": 0.1,
                "hops": 0,
                "path": [],
            }
        ],
        "expanded": [
            {
                **pages[3],
                "hops": 2,
                "path": [],
            }
        ],
        "max_hops": 2,
    }

    monkeypatch.setattr(
        "app.retrieval.search",
        lambda query: vector_hits,
    )
    monkeypatch.setattr(
        "app.retrieval.load_pages",
        lambda source: pages,
    )
    monkeypatch.setattr(
        "app.retrieval.search_graph",
        lambda query: graph_result,
    )

    results = search_hybrid("test query")

    assert [result["page_id"] for result in results] == [
        "doc-a-p002",
        "doc-a-p001",
        "doc-a-p003",
        "doc-a-p004",
    ]
    assert results[0]["retrieval_sources"] == [
        "vector",
        "graph_seed",
    ]
    assert results[1]["retrieval_sources"] == ["neighbor"]
    assert results[2]["retrieval_sources"] == ["neighbor"]
    assert results[3]["retrieval_sources"] == ["graph_expanded"]


def test_hybrid_removes_duplicate_pages(monkeypatch):
    pages = [
        make_page("doc-a-p001", 1),
        make_page("doc-a-p002", 2),
        make_page("doc-a-p003", 3),
    ]
    vector_hits = [
        {**pages[1], "distance": 0.1},
    ]
    graph_result = {
        "seeds": [{**pages[1], "hops": 0, "path": []}],
        "expanded": [{**pages[2], "hops": 1, "path": []}],
        "max_hops": 2,
    }

    monkeypatch.setattr(
        "app.retrieval.search",
        lambda query: vector_hits,
    )
    monkeypatch.setattr(
        "app.retrieval.load_pages",
        lambda source: pages,
    )
    monkeypatch.setattr(
        "app.retrieval.search_graph",
        lambda query: graph_result,
    )

    results = search_hybrid("test query")
    page_ids = [result["page_id"] for result in results]

    assert page_ids == [
        "doc-a-p002",
        "doc-a-p001",
        "doc-a-p003",
    ]
    assert len(page_ids) == len(set(page_ids))
    assert results[2]["retrieval_sources"] == [
        "neighbor",
        "graph_expanded",
    ]


def test_hybrid_respects_max_results(monkeypatch):
    pages = [
        make_page(f"doc-a-p{i:03d}", i)
        for i in range(1, 15)
    ]
    vector_hits = [
        {**page, "distance": index / 10}
        for index, page in enumerate(pages[:5])
    ]
    graph_result = {
        "seeds": [],
        "expanded": [
            {**page, "hops": 2, "path": []}
            for page in pages[5:]
        ],
        "max_hops": 2,
    }

    monkeypatch.setattr(
        "app.retrieval.search",
        lambda query: vector_hits,
    )
    monkeypatch.setattr(
        "app.retrieval.load_pages",
        lambda source: pages,
    )
    monkeypatch.setattr(
        "app.retrieval.search_graph",
        lambda query: graph_result,
    )
    monkeypatch.setattr(
        "app.retrieval.HYBRID_MAX_RESULTS",
        8,
    )

    results = search_hybrid("test query")

    assert len(results) == 8
    assert [result["page_id"] for result in results[:5]] == [
        page["page_id"] for page in pages[:5]
    ]
