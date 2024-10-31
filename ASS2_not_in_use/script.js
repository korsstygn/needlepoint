const researchQuestions = document.getElementById('research-questions');
const datasetQuestions = document.getElementById('dataset-questions');
const topKeywords = document.querySelectorAll('.top-keyword');
const articlesWithTopKeywords = document.querySelectorAll('.article-with-top-keywords');
const topAuthors = document.querySelectorAll('.top-author');

// assuming you have the data in the following format
let data = {
    research: 'This is a research question',
    dataset: 'This is a dataset question',
    keywords: [
        { keyword: 'Keyword 1', frequency: 10 },
        { keyword: 'Keyword 2', frequency: 20 },
        // ...
    ],
    articles: [
        {
            Url: 'https://example.com/article1',
            Title: 'Article 1',
            Description: 'This is the description of article 1',
            keywords: ['Keyword 1', 'Keyword 2'],
        },
        {
            Url: 'https://example.com/article2',
            Title: 'Article 2',
            Description: 'This is the description of article 2',
            keywords: ['Keyword 3', 'Keyword 4'],
        },
        // ...
    ],
    authors: [
        {
            Author: 'Author 1',
            Keywords: { Keyword 1: 10, Keyword 2: 20 },
        },
        {
            Author: 'Author 2',
            Keywords: { Keyword 3: 30, Keyword 4: 40 },
        },
        // ...
    ],
};

researchQuestions.textContent = data.research;
datasetQuestions.textContent = data.dataset;

topKeywords.forEach((keyword) => {
    const { keyword: k, frequency } = data.keywords