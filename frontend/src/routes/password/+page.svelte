<script>
	import { goto } from '$app/navigation';
    import { v4 as uuid } from 'uuid';

	async function postToBack() {
		const res = await fetch('http://127.0.0.1:8000/api', {
						method: 'POST',
						body: JSON.stringify({ len, useNumbers, useSpec, name }),
						headers: {
							'Content-Type': 'application/json'
						}
					});
		let answer = await getAnswerFromBack()
		return answer
	}

	async function getAnswerFromBack() {
		const res = await fetch('http://127.0.0.1:8000/get_from_db').then(
			res=> {
				return res.json()
			}
		);
		console.log(res)
		return res
	}

	async function getFromBack() {
		const res = await fetch('http://127.0.0.1:8000/api').then(
			res=> {
				return res.json()
			}
		);
		console.log(res)
		return res
	}

	let dat = getFromBack()
	let len = 6
	let useNumbers = false
	let useSpec = false

	let generatedPassword = {password: "None"}
	let showGenerator = true
	let name = ''
	let notFilled = true

	$: if (name != '') 
	{notFilled = false}
	else notFilled = true
</script>

<div class="main-container">
	<div class="blc-settings">
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<!-- svelte-ignore a11y-no-static-element-interactions -->
			<div class="section-nav-btn" on:click={()=>{goto('/list')}}>Show all</div>
			<h1>Customize your password</h1>

			<div class="section-col">
				<label for="length">Enter Name:</label>
				<input bind:value={name} type="text" id="name" class="name">
				{#if notFilled}
					<div class="warning">*This is a mandatory field to fill in</div>
				{/if} 
			</div>
			
			<!-- <div class="regular-text">Length:</div> -->
			<div class="section">
				<input bind:value={len} type="range" id="length" class="length" min="4" max="16">
				<label for="length">Length is: {len}</label>
			</div>

			<div class="section">
				<input bind:checked={useNumbers} type="checkbox" class="check" id="check1">
				<label for="check1">Use numbers</label>
			</div>

			<div class="section">
				<input bind:checked={useSpec} type="checkbox" class="check" id="check2">
				<label for="check2">Use special symbols</label>
			</div>

			<button class="generate-password" on:click={async(event) => {
				generatedPassword = await postToBack()
			}}>
				Generate password
			</button>

			<div>The password is: {generatedPassword.password}</div>
	</div>
</div>

<style>
	.warning {
		color: red;
	}
	.name {
		width: 200px;
	}
	.check {
		min-width: 15px;
		min-height: 15px;
	}
	.section-col {
		width:100%;
		margin-left: 16px;
		margin-bottom: 16px;
		display: flex;
		flex-direction: column;
		justify-content: left;
	}
	.section-nav-btn {
		position: absolute;
		top: 0;
		left: 0;
		margin-left: 8px;
		margin-top	: 8px;
	}
	.section {
		width:100%;
		margin-left: 16px;
		margin-bottom: 16px;
		display: flex;
		flex-direction: row;
		justify-content: left;
	}
	.blc-settings {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		width: 400px;
		height: 400px;
		border: 1px solid black;
		border-radius: 30px;
		background-color: #ede9e9;
	}
	.main-container {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		height: 600px;
		flex: 0.6;
	}

	h1 {
		margin-left: 16px;
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
