# github-stats

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)

GitHub Stats is a simple, free, and open-source GitHub profile statistics generator. This project was built using Python programming language with web framework Flask in accordance with GitHub API documentation. This project was inspired by [github-readme-stats](anuraghazra/github-readme-stats).

## Features 💡

Using Github Stats, you can:

- [x] Create and customize badge for your GitHub profile.
- [x] Use GitHub REST API to get the data.
- [x] Use GitHub GraphQL API to get the data.

## Usage 👨‍💻

Create your own badge by change the `USERNAME` and `THEME` in the URL below. Curently there are 2 themes available: `dark` and `light`.

```url
https://github-stats-putuwaw.vercel.app/api?username=USERNAME&theme=THEME
```

> [!NOTE]  
> You can also use the GraphQL API by using `/api/graphql` endpoint instead of REST API on `/api` endpoint.

Examples:

`Dark theme:`

[![](https://github-stats-putuwaw.vercel.app/api?username=putuwaw&theme=dark)](https://github-stats-putuwaw.vercel.app/api?username=putuwaw&theme=dark)

`Light theme:`

[![](https://github-stats-putuwaw.vercel.app/api?username=putuwaw&theme=light)](https://github-stats-putuwaw.vercel.app/api?username=putuwaw&theme=dark)

## Prerequisites 📋

- Python 3.10 or higher

## Installation 🛠

- Clone the repository:

```bash
git clone https://github.com/putuwaw/github-stats.git
```

- Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

- Install the dependencies:

```bash
make py-install
```

- Create .env file and set the environment variables for GitHub API:

```bash
make env
```

- Run the application:

```bash
make run
```

## Contributing 🤝

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License 📝

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
