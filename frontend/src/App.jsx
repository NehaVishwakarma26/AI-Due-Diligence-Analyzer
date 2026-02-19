import { useState } from "react"
import axios from "axios"

export default function App() {
  const [files, setFiles] = useState([])
  const [question, setQuestion] = useState("")
  const [response, setResponse] = useState(null)
  const [loading, setLoading] = useState(false)
  const [uploading, setUploading] = useState(false)
  const [domain,setDomain]=useState("")

  const uploadDocs = async () => {
    if (!files.length) return alert("Select files first")

    const formData = new FormData()
    for (let file of files) {
      formData.append("file", file)
formData.append("domain",domain)

    }

    setUploading(true)

    try {
      await axios.post(
        "http://localhost:8080/api/upload",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      )
      alert("Documents uploaded successfully!")
    } catch (err) {
      console.error(err)
      alert("Upload failed")
    }

    setUploading(false)
  }

  const askQuestion = async () => {
    setLoading(true)
    try {
      const res = await axios.post(
        "http://localhost:8080/api/ask",
        { question }
      )
      setResponse(res.data)
    } catch (err) {
      console.error(err)
      alert("Error querying backend")
    }
    setLoading(false)
  }

  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <div className="max-w-4xl mx-auto bg-white p-8 rounded-xl shadow-lg">

        <h1 className="text-3xl font-bold mb-8">
          AI Due Diligence Analyzer
        </h1>

        {/* Upload Section */}
        <div className="mb-10 border-b pb-6">
          <h2 className="text-xl font-semibold mb-4">
            Upload Company Documents
          </h2>

          <input
            type="file"
            multiple
            onChange={(e) => setFiles(e.target.files)}
            className="mb-4"
          />

          <input placeholder="Enter file domain... eg. Product" value={domain} onChange={(e)=>setDomain(e.target.value)}/>
<br></br>
          <button
            onClick={uploadDocs}
            className="bg-green-600 text-white px-6 py-2 rounded-lg"
          >
            {uploading ? "Uploading..." : "Upload"}
          </button>
        </div>

        {/* Ask Section */}
        <div>
          <h2 className="text-xl font-semibold mb-4">
            Ask a Question
          </h2>

          <textarea
            className="w-full border p-3 rounded-lg mb-4"
            rows="3"
            placeholder="Are there compliance risks?"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />

          <button
            onClick={askQuestion}
            className="bg-blue-600 text-white px-6 py-2 rounded-lg"
          >
            {loading ? "Analyzing..." : "Analyze"}
          </button>
        </div>

        {/* Response */}
        {response && (
  <div className="mt-10 space-y-6">

    {/* Answer */}
    <div>
      <h3 className="font-semibold text-lg">Answer</h3>
      <p>{response.answer ?? "No summary provided."}</p>
    </div>

    {/* Key Points */}
    <div>
      <h3 className="font-semibold text-lg">Key Points</h3>
      <ul className="list-disc pl-6">
        {response.key_points?.map((p, i) => (
          <li key={i}>
            {typeof p === "string" ? p : p.text}
          </li>
        ))}
      </ul>
    </div>

    {/* Risk Flags */}
    <div>
      <h3 className="font-semibold text-lg text-red-600">
        Risk Flags
      </h3>
      <ul className="list-disc pl-6">
        {response.risk_flags?.filter(Boolean).map((r, i) => (
          <li key={i}>
            {typeof r === "string" ? r : r?.text}
          </li>
        ))}
      </ul>
    </div>

    {/* Confidence */}
    <div>
      <h3 className="font-semibold text-lg">Confidence</h3>
      <p>{response.confidence_score}</p>
    </div>

  </div>
)}


      </div>
    </div>
  )
}
