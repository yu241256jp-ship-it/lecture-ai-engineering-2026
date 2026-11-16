from app.retrieval import add_neighbor_pages, search_with_neighbors


def make_page(page_id: str, document_id: str, page_number: int) -> dict:
    return {
        "page_id": page_id,
        "document_id": document_id,
        "lecture": 1,
        "document_title": document_id,
        "section": "section",
        "title": page_id,
        "page": page_number,
        "content": f"{page_id} content",
    }


def test_adds_previous_and_next_pages():
    pages = [
        make_page("doc-a-p001", "doc-a", 1),
        make_page("doc-a-p002", "doc-a", 2),
        make_page("doc-a-p003", "doc-a", 3),
    ]
    hits = [{**pages[1], "distance": 0.1}]

    results = add_neighbor_pages(hits, pages)

    assert [result["page_id"] for result in results] == [
        "doc-a-p002",
        "doc-a-p001",
        "doc-a-p003",
    ]
    assert results[0]["retrieval_source"] == "vector"
    assert results[1]["retrieval_source"] == "neighbor"
    assert results[1]["seed_page_id"] == "doc-a-p002"
    assert results[2]["seed_page_id"] == "doc-a-p002"


def test_does_not_cross_document_boundary():
    pages = [
        make_page("doc-a-p001", "doc-a", 1),
        make_page("doc-a-p002", "doc-a", 2),
        make_page("doc-b-p001", "doc-b", 1),
    ]
    hits = [{**pages[1], "distance": 0.1}]

    results = add_neighbor_pages(hits, pages)

    assert [result["page_id"] for result in results] == [
        "doc-a-p002",
        "doc-a-p001",
    ]


def test_removes_duplicates_when_neighbor_is_also_a_hit():
    pages = [
        make_page("doc-a-p001", "doc-a", 1),
        make_page("doc-a-p002", "doc-a", 2),
        make_page("doc-a-p003", "doc-a", 3),
    ]
    hits = [
        {**pages[1], "distance": 0.1},
        {**pages[2], "distance": 0.2},
    ]

    results = add_neighbor_pages(hits, pages)
    page_ids = [result["page_id"] for result in results]

    assert page_ids == [
        "doc-a-p002",
        "doc-a-p003",
        "doc-a-p001",
    ]
    assert len(page_ids) == len(set(page_ids))


def test_first_page_only_adds_next_page():
    pages = [
        make_page("doc-a-p001", "doc-a", 1),
        make_page("doc-a-p002", "doc-a", 2),
    ]
    hits = [{**pages[0], "distance": 0.1}]

    results = add_neighbor_pages(hits, pages)

    assert [result["page_id"] for result in results] == [
        "doc-a-p001",
        "doc-a-p002",
    ]


def test_empty_hits_return_empty_results():
    pages = [make_page("doc-a-p001", "doc-a", 1)]

    assert add_neighbor_pages([], pages) == []


def test_search_with_neighbors_uses_vector_hits(monkeypatch):
    pages = [
        make_page("doc-a-p001", "doc-a", 1),
        make_page("doc-a-p002", "doc-a", 2),
        make_page("doc-a-p003", "doc-a", 3),
    ]
    hits = [{**pages[1], "distance": 0.1}]

    monkeypatch.setattr("app.retrieval.search", lambda query: hits)
    monkeypatch.setattr("app.retrieval.load_pages", lambda source: pages)

    results = search_with_neighbors("test query")

    assert [result["page_id"] for result in results] == [
        "doc-a-p002",
        "doc-a-p001",
        "doc-a-p003",
    ]


def test_search_with_neighbors_preserves_incomplete_mock_hit(monkeypatch):
    hit = {
        "page_id": "lec02-main-p052",
        "lecture": 2,
        "page": 52,
        "content": "元の重みは固定",
    }
    monkeypatch.setattr("app.retrieval.search", lambda query: [hit])

    results = search_with_neighbors("LoRA")

    assert results == [hit]
