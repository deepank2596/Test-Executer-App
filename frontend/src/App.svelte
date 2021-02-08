<script>
	import axios from "axios"
	let filepath
	let tests=[]
	$: test_cases= tests.map(test=> {return {...test,status:"-",time_taken:"-"}})
	//testcases/basic_tests.json
	async function importTests(){
		try {
			let res = await axios.post("http://localhost:8000/api/getTestCases",{filepath})
			let data= await res.data
			tests=data
		} catch (error) {
			console.log(error)
		}
	}
	async function executeTests(){
		try {
			test_cases= test_cases.map(test=> {return {...test,status:"In Process"}})
				console.log(test_cases)
				let res = await axios.post("http://localhost:8000/api/execute",{"test_cases":JSON.stringify(test_cases)})
				let data= await res.data
				console.log(data)		
		} catch (error) {
			console.log(error)
		}
	}
</script>

<div class="main container">
	<div class="heading-container row bg-danger rounded">
		<h1 class="h1 text-center">Test Executer</h1>
	</div>
	<br><br>
	<div class="file-input row">
		<div class="col-1">
			<label for="file-path" class="form-label fw-bold pt-2">File Path</label>
		</div>
		<div class="col-8">
			<input id="file-path" bind:value="{filepath}" class="form-control" type="text" placeholder="Enter Test JSON file path here">
		</div>
		<div class="col-3">
			<button on:click="{importTests}" class="btn btn-primary">Import</button>
			<button on:click="{executeTests}" class="btn btn-primary">Run</button>
		</div>
	</div>
	<br><br>
	<div class="row p-3 text-dark bg-danger rounded">
		<div class="col-8">
		  <h1 class="h6 mb-0 lh-1">Test Cases</h1>
		</div>
		<div class="col-2">
			<h1 class="h6 mb-0 lh-1 text-center">Status</h1>
		</div>
		<div class="col-2">
			<h1 class="h6 mb-0 lh-1 text-center">Time Taken</h1>
		</div>
	</div>
	<div class="testcases pt-2">
	{#each test_cases as test, count}
	  	<div class="test row mb-2 border border-dark rounded p-3">
			  <div class="col-8">
				<h1  title="Steps" class="h6 fw-bold" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-content="{test.steps.map(step=>step.action)}">{count+1}. {test.name}</h1>
			  </div>
			  <dic class="col-2">
				<h1 class="h6 fw bold text-center">{test.status}</h1>
			  </dic>
			  <dic class="col-2">
				<h1 class="h6 fw bold text-center">{test.time_taken}</h1>
			  </dic>
		</div>
	{/each}
	</div>
</div>

